import requests

def main():
    print("Enter the base URL (e.g., https://example.com):")
    baseUrl = input()

    paths = [
        "/admin",
        "/login",
        "/wp-admin",  # Wordpress admin panel
        "/.git",  # Exposed .git directory
        "/.env",  # Exposed environment variables
        "/.htaccess",  # Exposed server configuration
        "/wp-content/", #wordpress content
        "/wp-includes/", #wordpress core
         "/wp-includes/",  # WordPress core files
        "/administrator/",  # Joomla admin login
        "/user/login",  # Drupal login page
        "/phpmyadmin/",  # phpMyAdmin database manager
        "/phppgadmin/",  # phpPgAdmin database manager for PostgreSQL
        "/adminer.php",  # Adminer database management tool
        "/.svn/",  # Exposed Subversion directory
        "/.git/config",  # Exposed .git configuration
        "/robots.txt",  # Robots.txt file
        "/.htaccess",  # Apache server configuration
        "/.htpasswd",  # Apache password file
        "/.bash_history",  # Bash history file
        "/.DS_Store",  # macOS folder settings
        "/backup.tar.gz",  # Possible backup file
        "/backup.zip",  # Possible backup file
        "/database.sql",  # Possible backup file
        "/error.log",  # Server error logs
        "/install.php",  # CMS setup files
        "/setup.php",  # CMS setup files
        "/readme.html",  # Application readme
        "/README.md",  # Application readme
        "/cpanel/",  # cPanel login
        "/webmail/",  # Webmail login
        "/swag/",  # Swagger UI
        "/_profiler/",  # Symfony web debug toolbar
        "/info.php",  # File with phpinfo() output
        "/apidoc/",  # API documentation
        "/api/",  # Common API endpoint
        "/graphql",  # GraphQL endpoint
        "/api/debug",  # Possible debugging endpoint for APIs
        "/.git"  # Exposed .git directory
        "/phpinfo.php", # File with phpinfo() output
        "/info.php",
        "/.env",  # Exposed environment variables
        "/test.php",
        "/backup",
        "/db_backup",
        "/backup.sql",
        "/db_backup.sql",
        "/config.php",  # Common configuration file
        "/wp-config.php",  # WordPress configuration file
        "/sitemap.xml",  # May give a layout of all the URLs of the application

    ]

    for path in paths:
        url = baseUrl.rstrip('/') + path
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"[!] Potential Issue Found at: {url}")
        except Exception as e:
            print(f"[ERROR] Could not scan {url}. Reason: {str(e)}")

    print("Scan Complete.")

if __name__ == '__main__':
    main()
