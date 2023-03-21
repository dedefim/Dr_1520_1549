import React from 'react'


const FootItem = ({foot}) => {
    return (
        <tr>
            <td>
                {foot.name}
            </td>
            <td>
                {foot.age}
            </td>
            <td>
                {foot.win}
            </td>

        </tr>
    )
}
const FootList = ({footers}) => {
    return (
        <table>
            <th>
                Name
            </th>
            <th>
                Age
            </th>
            <th>
                Win
            </th>

            {footers.map((foot) => <FootItem foot={foot} />)}
        </table>
    )
}
export default FootList