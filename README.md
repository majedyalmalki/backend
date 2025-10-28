<h1>Back End</h1>

<h3>ERD: 🖇️</h3>
<img src="./assets/images/PlantsERD.svg">

<br />
<br />

<table border="1" width="100%">
    <thead>
    <h2>User</h2>
        <tr>
            <th width="15%">Entity</th>
            <th width="25%">HTTP Method</th>
            <th width="50%">Endpoint</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>User</td><td>GET</td><td>/User</td></tr>
        <tr><td>User</td><td>GET</td><td>/User/{id}</td></tr>
        <tr><td>User</td><td>POST</td><td>/User</td></tr>
        <tr><td>User</td><td>PUT</td><td>/User/{id}</td></tr>
        <tr><td>User</td><td>DELETE</td><td>/User/{id}</td></tr>
    </tbody>
</table>


<table border="1" width="100%">
    <thead>
    <h2>Plant</h2>
        <tr>
            <th width="15%">Entity</th>
            <th width="25%">HTTP Method</th>
            <th width="50%">Endpoint</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Plant</td><td>GET</td><td>/Plant</td></tr>
        <tr><td>Plant</td><td>GET</td><td>/Plant/{id}</td></tr>
        <tr><td>Plant</td><td>POST</td><td>/Plant</td></tr>
        <tr><td>Plant</td><td>PUT</td><td>/Plant/{id}</td></tr>
        <tr><td>Plant</td><td>DELETE</td><td>/Plant/{id}</td></tr>
    </tbody>
</table>


<table border="1" width="100%">
    <thead>
    <h2>Reminder</h2>
        <tr>
            <th width="15%">Entity</th>
            <th width="25%">HTTP Method</th>
            <th width="50%">Endpoint</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Reminder</td><td>GET</td><td>/Reminder</td></tr>
        <tr><td>Reminder</td><td>GET</td><td>/Reminder/{id}/Plant{id}</td></tr>
        <tr><td>Reminder</td><td>POST</td><td>/Reminder</td></tr>
        <tr><td>Reminder</td><td>PUT</td><td>/Reminder/{id}/Plant{id}</td></tr>
        <tr><td>Reminder</td><td>DELETE</td><td>/Reminder/{id}/Plant{id}</td></tr>
    </tbody>
</table>


<table border="1" width="100%">
    <thead>
    <h2>Location</h2>
        <tr>
            <th width="15%">Entity</th>
            <th width="25%">HTTP Method</th>
            <th width="50%">Endpoint</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Location</td><td>GET</td><td>/Location</td></tr>
        <tr><td>Location</td><td>GET</td><td>/Location/{id}/Plant{id}</td></tr>
        <tr><td>Location</td><td>POST</td><td>/Location</td></tr>
        <tr><td>Location</td><td>PUT</td><td>/Location/{id}/Plant{id}</td></tr>
        <tr><td>Location</td><td>DELETE</td><td>/Location/{id}/Plant{id}</td></tr>
    </tbody>
</table>