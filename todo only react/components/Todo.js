import React from "react";
import TodoForm from "./TodoForm";
import Strike from './Strike';

export default class Todo extends React.Component {
    state = {
        todos: [],
        toShow: "all"
    };
    addTodo = todo => {
        this.setState({
            todos: [todo, ...this.state.todos]
        });
    };

    toggleComplete = id => {
        this.setState({
            todos: this.state.todos.map(todo => {
                if (todo.id === id) {
                    return {
                        // id: todo.id,
                        // text: todo.text,
                        ...todo,
                        complete: !todo.complete
                    };
                } else {
                    return todo;
                }
            })
        });
    }

    updateToShow = (s) => {
        this.setState({
            toShow: s
        })
    }

    handleDel = id => {
        this.setState({
            todos: this.setState.filter(todo => todo.id !== id)
        });
    };


    render() {
        let todos = []

        if (this.state.toShow === 'all') {
            todos = this.state.todos;
        } else if (this.state.toShow === 'active') {
            todos = this.state.todos.filter(todo => !todo.complete);
        } else if (this.state.toShow === 'complete') {
            todos = this.state.todos.filter(todo => todo.complete);
        }
        return (
            <div>
                <TodoForm onSubmit={this.addTodo} />
                {todos.map(todo => (
                    <Strike key={todo.id} toggleComplete={() => this.toggleComplete(todo.id)}
                        onDelete={() => this.handleDel(todo.id)} todo={todo} />
                ))}
                <div>Tasks left:{this.state.todos.filter(todo => !todo.complete).length}</div>
                <div>
                    <button onClick={() => this.updateToShow("all")}>all</button>
                    <button onClick={() => this.updateToShow("active")}>active</button>
                    <button onClick={() => this.updateToShow("complete")}>complete</button>
                </div>
            </div>
        );
    }
}


