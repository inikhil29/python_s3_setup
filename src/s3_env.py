from s3_utils import get_s3_env_variables, initialize_s3_resource

if __name__ == "__main__":

        s3_env_vars = get_s3_env_variables()
        s3_resource = initialize_s3_resource(s3_env_vars['aws_access_key'], s3_env_vars['aws_secret_key'], s3_env_vars['region'])  
        print(s3_resource)