import React, { Component } from 'react';
import './App.css';
import Todo from '.components/Todo';

class App extends Component {
    state = {
        count: 0
    };
    increment = () => {
        this.setState({
            count: this.state.count + 1
        });
    };

    decrement = () => {
        this.setState({
            count: this.state.count - 1
        });
    };

    render() {
        return (
            <div className="App">
                <Todo />
            </div>
        );
    }
}
export default App;

