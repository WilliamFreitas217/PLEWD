import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import { ThemeProvider } from '@material-ui/styles';
import { createMuiTheme } from '@material-ui/core/styles';

import Footer from '../../Components/Footer/Footer';
import Header from '../../Components/Header/Header';
import complex from '../../Assets/Shelby.jpg';
import Fab from '@material-ui/core/Fab';
import AddIcon from '@material-ui/icons/Add';
import { IconButton } from '@material-ui/core';
import DeleteIcon from '@material-ui/icons/Delete';
import Menu from '../../Components/Menu/Menu';

const theme=createMuiTheme({
  "palette":{"common":{"black":"#000","white":"#fff"},"background":{"paper":"#fff","default":"#fafafa"},"primary":{"light":"rgba(255, 128, 171, 1)","main":"rgba(255, 64, 129, 1)","dark":"rgba(197, 17, 98, 1)","contrastText":"#fff"},"secondary":{"light":"rgba(179, 157, 219, 1)","main":"rgba(126, 87, 194, 1)","dark":"rgba(103, 58, 183, 1)","contrastText":"#fff"},"error":{"light":"rgba(234, 128, 252, 1)","main":"rgba(224, 64, 251, 1)","dark":"rgba(213, 0, 249, 1)","contrastText":"#fff"},"text":{"primary":"rgba(0, 0, 0, 0.87)","secondary":"rgba(0, 0, 0, 0.54)","disabled":"rgba(0, 0, 0, 0.38)","hint":"rgba(0, 0, 0, 0.38)"}}
 })

const useStyles = makeStyles({
  root: {
    justifyContent: "center",
  },
  card: {
    marginLeft:26,
    minWidth: 300,
    maxWidth: 345,
    flexGrow: 'flex',
    flexDirection: 'row'
  },
  media: {
    height: 140,
  },
  fab: {
    position: 'fixed',
    bottom: theme.spacing(10),
    right: theme.spacing(2),
  },
  icon: {

  }
});


const list = [
  {
    id: 'abcde123',
    vendedor: 'Robin',
    produto: 'Trufa',
    preco: 19.88,
    pic: complex,
  },
  {
    id: 'bcdef123',
    vendedor: 'Robin',
    produto: 'Brigadeiro',
    preco: 1.50,
    pic: complex,
  },

  {
    id: 'cdefgh123',
    vendedor: 'Robin',
    produto: 'Trufa',
    preco: 19.88,
    pic: complex,
  },
  {
    id: 'defghi123',
    vendedor: 'Robin',
    produto: 'Brigadeiro',
    preco: 1.50,
    pic: complex,
  },
  {
    id: 'efghij123',
    vendedor: 'Robin',
    produto: 'Trufa',
    preco: 19.88,
    pic: complex,
  },
];

export default function Lista() {
  const classes = useStyles();
  

  return (
    < ThemeProvider theme = {theme} >
      <Menu></Menu>
    <div className={classes.root}>
      {list.map(item => (
        <Button onClick = {() => { window.open('http://localhost:3000/produtoperfil', '_self'); }}>
        <Card className={classes.card}>
      <CardActionArea>
        <CardMedia
          className={classes.media}
          image={item.pic}
          title="Contemplative Reptile"
        />
        <CardContent>
          <Typography gutterBottom variant="h4" component="h2">
            {item.produto}
          </Typography>

          <Typography gutterBottom variant="h5" component="h2">
            R$ {item.preco}
          </Typography>
          
        </CardContent>
      </CardActionArea>
    </Card>
    </Button>
      ))}
    
    <Footer></Footer>
    </div>
    <Fab color="primary" className={classes.fab} href="/novo">   
      <AddIcon/>
    </Fab>
    </ThemeProvider>
  );
}