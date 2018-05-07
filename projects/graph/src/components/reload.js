import React from 'react';

const reloadStyle = {
  margin: '50px auto',
};

const buttonStyle = {
  // width: '200px',
  // height: '24px',
  // background: 'black',
  // color: 'white',
  // border: 'none',
  // outline: 'none',
  fontSize: '12px',
};

// const hoverButtonHandler = _ => {
// buttonStyle.background = 'white';
// buttonStyle.color = 'white';
// };

const reloadButtonClickedHandler = props => {
  props.reloadButtonClicked();
};

const ReloadButton = props => {
  return (
    <div className="Reload" style={reloadStyle}>
      <button
        type="button"
        className="ReloadButton"
        style={buttonStyle}
        // onMouseEnter={hoverButtonHandler}
        onClick={_ => reloadButtonClickedHandler(props)}
      >
        reload
      </button>
    </div>
  );
};

export default ReloadButton;
