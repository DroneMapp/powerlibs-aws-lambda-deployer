import powerlibs.aws.λ.deployer
from powerlibs.aws.λ.deployer import settings
from powerlibs.aws.λ.deployer.lambda_settings import load_settings


if __name__ == '__main__':
    lambda_settings = load_settings(settings.LAMBDA_SETTINGS_FILE)
    powerlibs.aws.λ.deployer.main(lambda_settings)
