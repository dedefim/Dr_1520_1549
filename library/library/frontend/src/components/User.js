import React from 'react'


const UserItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.user.name}</td>
            <td><button type='button'>Delete</button></td>
        </tr>
       )
}
const UserList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>User</th>
                <th></th>
            </tr>
            {items.map((item) => <UserItem item={item} />)}
        </table>
    )
}
export default BookList

const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.birthday_year}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}
const UserList = ({users}) => {
    return (
        <table>
            <th>
                First name
            </th>
            <th>
                Last Name
            </th>
            <th>
                Birthday year
            </th>
            <th>
                Email
            </th>
            {users.map((user) => <UserItem user={user} />)}
        </table>
    )
}
export default UserList