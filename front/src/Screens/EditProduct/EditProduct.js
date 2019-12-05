import React from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import { makeStyles, ThemeProvider } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import { createMuiTheme } from '@material-ui/core/styles';
import UploadButtons from '../../Components/UploadButton/Upload';
import Menu from '../../Components/Menu/Menu';
import Footer from '../../Components/Footer/Footer';

const theme=createMuiTheme({
  "palette":{"common":{"black":"#000","white":"#fff"},"background":{"paper":"#fff","default":"#fafafa"},"primary":{"light":"rgba(255, 128, 171, 1)","main":"rgba(255, 64, 129, 1)","dark":"rgba(197, 17, 98, 1)","contrastText":"#fff"},"secondary":{"light":"rgba(179, 157, 219, 1)","main":"rgba(126, 87, 194, 1)","dark":"rgba(103, 58, 183, 1)","contrastText":"#fff"},"error":{"light":"rgba(234, 128, 252, 1)","main":"rgba(224, 64, 251, 1)","dark":"rgba(213, 0, 249, 1)","contrastText":"#fff"},"text":{"primary":"rgba(0, 0, 0, 0.87)","secondary":"rgba(0, 0, 0, 0.54)","disabled":"rgba(0, 0, 0, 0.38)","hint":"rgba(0, 0, 0, 0.38)"}}
})

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="https://material-ui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const useStyles = makeStyles(theme => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(3),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

export default function EditProduct() {
  const classes = useStyles();

  return (
    < ThemeProvider theme = {theme} >
    <Menu/>
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          <UploadButtons />
        </Avatar>
        <Typography component="h1" variant="h5">
          Editar Produto
        </Typography>
        <form className={classes.form} noValidate>
          <Grid container spacing={2}>
            <Grid item xs={12}>
              <TextField
                autoComplete="fname"
                name="firstName"
                variant="outlined"
                required
                fullWidth
                id="nome"
                label="Nome"
                autoFocus
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="qtd"
                label="Quantidade"
                name="qtd"
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="valor"
                label="Valor"
                type="valor"
                id="valor"
                autoComplete="current-password"
              />
            </Grid>

            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="desc"
                label="Descrição"
                id="desc"
              />
            </Grid>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
          >
            Salvar
          </Button>

          </Grid>
        </form>
      </div>
      <Box mt={5}>
        <Copyright />
      </Box>
    </Container>
    <Footer/>
    </ThemeProvider>
  );
}