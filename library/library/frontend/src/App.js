import React from 'react';
import axios from 'axios';
import './App.css';
import UserList from './components/User.js';
import MenuList from './components/Menu.js';
import FootList from './components/Foot.js';


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': []
        }
   }
   componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users').then(response => {
                const users = response.data
                    this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))
   }


   render () {
        return (
            <div>
                <UserList users={this.state.users} />
            </div>
        )
   }
}
class Menu extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'menus': []
        }
    }
    componentDidMount() {
        const menus = [
            {
                'soup': 'Щи',
                'miancourse': 'Котлета по киевски',
                'salat': 'Цезарь'
            },
            {
                'soup': 'Уха',
                'miancourse': 'Пельмени',
                'salat': 'Оливье'
            },
        ]
        this.setState(
            {
                'menus': menus
            }
        )
    }
    render () {
        return (
            <div>
                <MenuList menus={this.state.menus} />
            </div>
        )
    }
}
class Foot extends React.Component {
    render () {
        return (
            <div>
                <FootList footers={this.state.footers} />
                <MenuList menus={this.state.menus} />
                <UserList users={this.state.users} />
            </div>
        )
    }
}
export default App, Menu, Foot;