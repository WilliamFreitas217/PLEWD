import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import CssBaseline from '@material-ui/core/CssBaseline';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';


import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import HomeIcon from '@material-ui/icons/Home';
import PersonIcon from '@material-ui/icons/Person';

const useStyles = makeStyles(theme => ({
  text: {
    padding: theme.spacing(2, 2, 0),
  },
  paper: {
    paddingBottom: 50,
  },
  appBar: {
    top: 'auto',
    bottom: 0,
  },
  grow: {
    flexGrow: 1,
  },
  fabButton: {
    position: 'absolute',
    zIndex: 1,
    top: -30,
    left: 0,
    right: 0,
    margin: '0 auto',
  },
}));

export default function Footer() {
  const classes = useStyles();

  return (
    <React.Fragment>
      <CssBaseline />
      <AppBar position="fixed" color="primary" className={classes.appBar}>
        <Toolbar>
          <IconButton edge="start" color="inherit" aria-label="open drawer" onClick = {() => { window.open('http://localhost:3000/produtos', '_self'); }}>
            <ShoppingCartIcon/>
          </IconButton>

          <IconButton edge="end" color="inherit" onClick = {() => { window.open('http://localhost:3000/produtos', '_self'); }}>
            <HomeIcon/>
          </IconButton>

          <IconButton edge="end" color="inherit" onClick = {() => { window.open('http://localhost:3000/perfil', '_self'); }}>
            <PersonIcon/>
          </IconButton>
        </Toolbar>
      </AppBar>
    </React.Fragment>
  );
}
