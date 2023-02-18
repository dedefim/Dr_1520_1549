import React from 'react'
import AuthorList from './components/Author.js'
import BookList from './components/Book.js'

class App extends React.Component {
    constructor(props) {
        super(props)
        const TODO1 = {text: 'Hellow world', project:project1}
        const TODO2 = {text: "Hellow, EFIM", project:project2}
        const todos = [todos1, todos2]
        const project1 = {title: "1", link: 'Алые паруса',}
        const project2 = {title: "2", link: 'Золотая цепь'}
        this.state = {
            'TODO': todos,
            'project': project

        }
    }
render() {
    return (
        <div className="App">
            <HashRouter>
            <nav>
                <ul>
                    <li>
                        <Link to='/'>User</Link>
                    </li>
                    <li>
                        <Link to='/todo'>TODOList</Link>
                    </li>
                    <li>
                        <Link to='/project'>ProjectList</Link>
                    </li>
                </ul>
            </nav>
                            <Route exact path='/' component={() => <TODOList
items={this.state.todos} />} />
                           <Route exact path='/books' component={() => <ProjectList
items={this.state.project} />} />
            </HashRouter>
          </div>
        )
    }
}
export default App;