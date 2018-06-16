import React from 'react';
import { Button } from 'reactstrap';
import './button.css';

class Refresh extends React.Component {


render() {
    return (
        <div>
        <Button onClick={this.props.onClick}className="button" color="success" type="submit">RANDOMIZE GRAPH</Button>
        </div>
        )
    }
}

export default Refresh;