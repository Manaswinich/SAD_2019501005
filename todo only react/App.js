import React, { Component } from 'react';
import './App.css';
import Todo from './Todo';

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

}