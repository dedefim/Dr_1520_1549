import React from 'react';
import axios from 'axios';
import './App.css';
import UserList from './components/User.js';
import MenuList from './components/Menu.js';
import FootList from './components/Foot.js';
import LoginForm from './components/User.js'
import {BrowserRouter, Route, Switch, Redirect, Link} from 'react-router-dom'
import axios from 'axios'
import Cookies from 'universal-cookie';


get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username,
password: password})
    .then(response => {
        console.log(response.data)
    }).catch(error => alert('Неверный логин или пароль'))
    }

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

render() {
    return (
        <div className="App">
            <BrowserRouter>
                <nav>
                <ul>
                <li>
                <Link to='/user'>User</Link>
                </li>
                </ul>
            </nav>
                <Switch>
                            <Route exact path='/' component={() => <UserList
items={this.state.users} />} />
                <Route path="/users/:id">
                    <UserList items={this.state.books} />
                </Route>
                <Redirect from='/users' to='/' />
                <Route component={NotFound404} />
            </Switch>
        </BrowserRouter>
    </div>
    )
}

render() {
    return (
                    <Route exact path='/login' component={() => <LoginForm
get_token={(username, password) => this.get_token(username, password)} />} />


export default App, Menu, Foot;
