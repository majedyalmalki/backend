<h1>Back End</h1>

<h3>ERD: 🖇️</h3>
<img src="./assets/images/PlantsERD.svg">

<br />
<br />

<table border="1" width="100%">
    <thead>
    <h2>User</h2>
        <tr>
            <th width="15%">HTTP Method</th>
            <th width="25%">Path</th>
            <th width="50%">description</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>POST</td><td>"/user/signup/"</td><td>Endpoint for user registration.</td></tr>
        <tr><td>GET</td><td>"/user/login/"</td><td>Endpoint for user login.</td></tr>
        <tr><td>GET</td><td>"/user/token/refresh/"</td><td>Endpoint for refreshing user authentication tokens.</td></tr>
    </tbody>
</table>


<table border="1" width="100%">
    <thead>
    <h2>Plant</h2>
        <tr>
            <th width="15%">HTTP Method</th>
            <th width="25%">PATH</th>
            <th width="50%">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>GET</td><td>/plant</td><td>Retrieves a list of all plants.</td></tr>
        <tr><td>GET</td><td>/plant/{id}</td><td>Retrieves details of a specific plant identified by id.</td></tr>
        <tr><td>POST</td><td>/plant</td><td>Creates a new plant entry.</td></tr>
        <tr><td>PUT</td><td>/plant/{id}</td><td>Updates details of an existing plant identified by id.</td></tr>
        <tr><td>DELETE</td><td>/plant/{id}</td><td>Deletes a specific plant identified by id.</td></tr>
    </tbody>
</table>


<table border="1" width="100%">
    <thead>
    <h2>Reminder</h2>
        <tr>
            <th width="15%">HTTP Method</th>
            <th width="25%">PATH</th>
            <th width="50%">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>GET</td><td>/plant/{id}/reminder</td><td>Retrieves reminders for a specific plant identified by id.</td></tr>
        <tr><td>POST</td><td>/plant/{id}/reminder</td><td>Creates a new reminder for a specific plant.</td></tr>
        <tr><td>PUT</td><td>/reminder/{id}</td><td>Updates an existing reminder identified by id.</td></tr>
        <tr><td>DELETE</td><td>/reminder/{id}</td><td>Deletes a specific reminder identified by id.</td></tr>
    </tbody>
</table>


<table border="1" width="100%">
    <thead>
    <h2>Location</h2>
        <tr>
            <th width="15%">HTTP Method</th>
            <th width="25%">PATH</th>
            <th width="50%">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>GET</td><td>/location</td><td>Retrieves a list of all locations.</td></tr>
        <tr><td>POST</td><td>/location</td><td>Creates a new location entry.</td></tr>
        <tr><td>DELETE</td><td>/location/{id}</td><td>Deletes a specific location identified by id.</td></tr>
    </tbody>
</table>

<table border="1" width="100%">
    <thead>
    <h2>Plant & Location Relation</h2>
        <tr>
            <th width="15%">HTTP Method</th>
            <th width="25%">PATH</th>
            <th width="50%">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>GET</td><td>plant/{id}/location</td><td>Retrieves the location of a specific plant.</td></tr>
        <tr><td>PUT</td><td>plant/{id}/location/{id}</td><td>Updates the location of a plant.</td></tr>
        <tr><td>DELETE</td><td>plant/{id}/location/{id}</td><td>Deletes the relationship between a specific plant and its location.
</td></tr>
    </tbody>
</table>