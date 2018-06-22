import { StyleSheet, Platform } from 'react-native';
const styles = StyleSheet.create({
    headerStyle: {
        backgroundColor: '#007300',
        height: 50,
        paddingTop: Platform.OS === "android" ? 2 : 0,
        // paddingTop: 18,
        // marginTop: Platform.OS === "android" ? 18 : 0,
        // backgroundColor: 'gray',
    },
    carding: {
        margin: 20,
        marginLeft: 10,
        width : 360
    },
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center', 
    },
    titleStyle: {
        color: 'white',
        // alignItems: 'center',
        alignSelf: 'center'
    },
    buttonStyle: {
      margin:10,
      borderRadius:10,
    },
    logoutbuttonStyle: {
      margin:10,
      backgroundColor : 'white',
      borderColor: 'red',
      borderRadius:10,
      borderWidth: 1,
    },
    buttonTextStyle: {
        color: 'white'
    },
    logoutbuttonTextStyle: {
      color: 'red'
    },
    cardImage: {
      width: 360,
      height: 135,
      padding: 0,
      margin: 0,
      resizeMode: 'contain',
      alignSelf: 'center',
    },
    logo: {
        // flex: 1,
        justifyContent: 'center',
        marginTop: 70,
        marginBottom: 50,
        width: 250,
        height: 250,
        resizeMode: 'contain',
        alignSelf: 'center',
    },
    labelStyle: {
        color: 'white',
    },
    inputTextStyle: { 
        color: 'white' 
    },
  
    photoProfile:{
        fontSize : 100,
        alignSelf: 'center',
        paddingTop: 30,
    },
  
    emailIcon:{
      fontSize : 50,
      alignSelf: 'flex-start',
      paddingLeft : 20,
      paddingTop :5
    },
    phoneIcon:{
      fontSize : 50,
      alignSelf: 'flex-start',
      paddingLeft : 20,
      marginRight: 10,
      paddingTop :5
    },
    addressIcon:{
      fontSize : 50,
      alignSelf: 'flex-start',
      paddingLeft : 20,
      marginRight: 18,
      paddingTop :5
    },
    nama :{
        fontSize : 28,
        alignSelf: 'center',
        paddingTop: 0,
        paddingBottom: 0,
    },
    hairStyle: {
      backgroundColor: '#A2A2A2',
      height: 1,
      width: 340,
      marginTop: 0,
      marginLeft:20,
      marginRight: 20,
      marginBottom: 10
    },
    hairStyles: {
      backgroundColor: '#A2A2A2',
      height: 1,
      width: 260,
      marginTop: 0,
      marginLeft:100,
      marginRight:100,
      marginBottom: 5
    },
    email : {
      fontSize : 20,
      paddingLeft: 40,
      paddingTop: 0,
      paddingBottom:0
      },
    emails :{
      fontSize : 18,
      paddingLeft: 40,
      color : '#A2A2A2',
      paddingTop: 5,
      paddingBottom: 10,
      },
    row :{
        flexDirection: 'row',
    },
    kematangan1 :{
        marginTop: 20,
        paddingLeft: 20,
        fontSize: 20,
        fontWeight: 'bold'
    },
    berat1 :{
        marginTop: 20, 
        paddingLeft: 20,
        fontSize: 20,
        fontWeight: 'bold'
    },
    kematangan2 :{
        marginTop: 10,
        paddingLeft: 30,
        fontSize: 20,
    },
    berat2 :{
        marginTop: 10, 
        paddingLeft: 60,
        fontSize: 20,
    }
  
  });

  export default styles;