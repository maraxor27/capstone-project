# How to develop the API

There are README.md in each section that are related to the api. They can be followed like a tutorial. 
1. model/README.md - how to add a table in the database
2. router/README.md - how to add endpoints for the database table
3. dataAccessLayer/README.md - how to add function to manage the data in the database table.

Those README file do not explain all the aspect of the library used. However, they still are a good example to follow. Information about those library can be easily found on the internet with a quick google search using the name of the library. If you're not sure what library is being used, check at the top of the file for the source of the function or the class being used.

# TODO: How to develop a vue component and use Axios to make request to the API


# Database migration 
1. Get a terminal into the server container
> sudo docker exec -it capstone-project_web_server_1 /bin/bash
2. If the src/migrations folder doesn't exist, create it with 
> flask db init
3. Migrate the database
> flask db migrate -m "some message saying the modification"
4. Upgrade teh database
> flask db upgrade
5. Login to the database to ensure the change have occured
>psql -h postgres -p 5432 -d test -U user -W
The password will be asked. Go in database.env to find the password for user.
6. Look for the changes. This can be done in many way.
If you want to check for new table
> \dt
If you want to check a specific table
> select * from TABLE_NAME;
