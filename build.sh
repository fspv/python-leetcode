cur_dir=$(pwd)
tmp_dir=$(mktemp -d)

cd $tmp_dir
mkdir test

wget https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.27/swagger-codegen-cli-3.0.27.jar -O swagger-codegen-cli.jar


cd $cur_dir

java -jar $tmp_dir/swagger-codegen-cli.jar generate --help
_JAVA_OPTIONS="--add-opens=java.base/java.util=ALL-UNNAMED" java -jar $tmp_dir/swagger-codegen-cli.jar generate -l python -i swagger.yml -DpackageName=leetcode --git-user-id=prius --git-repo-id=python-leetcode


rm -rf $tmp_dir

patch -p1 < fix_cookies.patch
patch -p1 < fix_thread_pool.patch
patch -p1 < fix_gitignore.patch
