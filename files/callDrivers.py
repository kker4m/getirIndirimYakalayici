from otherFunctions import  *

class ChromeWithPrefs(webdriver.Chrome):
    def __init__(self, *args, options=None,profileName, **kwargs):
        if options:
            self.handle_prefs(options,profileName)

        super().__init__(*args, options=options, **kwargs)

        # remove the user_data_dir when quitting
        self.keep_user_data_dir = True

    @staticmethod
    def handle_prefs(options,profileName):
        if prefs := options.experimental_options.get("prefs"):
            # turn a (dotted key, value) into a proper nested dict
            def undot_key(key, value):
                if "." in key:
                    key, rest = key.split(".", 1)
                    value = undot_key(rest, value)
                return {key: value}

            # undot prefs dict keys
            undot_prefs = reduce(lambda d1, d2: {**d1, **d2},  # merge dicts
                (undot_key(key, value) for key, value in prefs.items()), )

            # create an user_data_dir and add its path to the options
            if profileName != None:
                user_data_dir = parentFolder + "driver" + seperator + "chromeLog"
                options.add_argument(f"--user-data-dir={user_data_dir}")

                # create the preferences json file in its default directory
                default_dir = os.path.join(user_data_dir, profileName)
                # os.mkdir(default_dir)

                prefs_file = os.path.join(default_dir, "Preferences")
                with open(prefs_file, encoding="latin1", mode="w") as f:
                    json.dump(undot_prefs, f)

            # pylint: disable=protected-access
            # remove the experimental_options to avoid an error
            del options._experimental_options["prefs"]

def callUcDriver(headless=False,profileName=None):
    prefs = {'download.default_directory': parentFolder + "images" + seperator, 'intl.accept_languages': 'en,en_US'}
    caps = DesiredCapabilities().CHROME


    caps["pageLoadStrategy"] = "normal"
    op = webdriver.ChromeOptions()
    if headless:
        op.headless = True

    # Sertifika hatasi alinmasi dahilinde,
    # python -m seleniumwire extractcert ile indirdiginiz
    # sertifikayi chrome'a ekleyiniz.

    op.add_argument('--ignore-certificate-errors')

    op.add_experimental_option("prefs", prefs)
    op.add_argument("--no-sandbox")
    op.add_argument("--disable-dev-shm-usage")
    op.add_argument("--disable-browser-side-navigation")
    op.add_argument("--dns-prefetch-disable")
    op.add_argument("--disable-gpu")

    op.add_argument("--disable-user-media-security=true")
    op.add_argument("--disable-popup-blocking")

    driver = ChromeWithPrefs(options=op,
                             driver_executable_path=parentFolder + "driver" + seperator + "chromedriver",
                             desired_capabilities=caps,profileName=profileName)
    return driver


if __name__ == "__main__":
    pass