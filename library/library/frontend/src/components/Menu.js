import React from 'react'


const MenuItem = ({menu}) => {
    return (
        <tr>
            <td>
                {menu.soup}
            </td>
            <td>
                {menu.miancourse}
            </td>
            <td>
                {menu.salat}
            </td>

        </tr>
    )
}
const MenuList = ({menus}) => {
    return (
        <table>
            <th>
                Soup
            </th>
            <th>
                Main course
            </th>
            <th>
                Salat
            </th>

            {menus.map((menu) => <MenuItem menu={menu} />)}
        </table>
    )
}
export default MenuList