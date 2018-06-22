import React from "react";
import { DrawerNavigator } from "react-navigation";
import {
  View,
  StyleSheet,
  ImageBackground,
  Image,
  Platform,
  KeyboardAvoidingView,
  StatusBar,
  AsyncStorage,
  TouchableOpacity,
  ActivityIndicator
} from "react-native";
import {
  Button,
  Text,
  Container,
  Card,
  CardItem,
  Body,
  Content,
  Header,
  Title,
  Left,
  Icon,
  Right,
  Input
} from "native-base";
import { ScrollView } from 'react-native-gesture-handler';
import { NavigationActions } from 'react-navigation'
import ImagePicker from 'react-native-image-picker'
import RNFetchBlob from 'react-native-fetch-blob'
import styles from './styles';

var options = {
  title: 'Select Photo',
  takePhotoButtonTitle: 'Take a Photo',
  chooseFromLibraryButtonTitle: 'Choose from gallery',
  quality: 1
};


export default class Main extends React.Component {
  constructor(props) {
    super(props)
    //    console.error(data)
  }
  state = {
    gambar : false,
    imageSource: null,
    data: null,
    loading: false,
    kematangan: null,
    berat: null
  }

  async fetchProfile() {
    try {
      const value = await AsyncStorage.getItem('user-profile');
      let parsed = JSON.parse(value)
      if (value !== null) {
        // We have data!!
        this.setState({
          id: parsed.id,
          nama: parsed.name,
          email: parsed.email,
          hp: parsed.phone,
          alamat: parsed.address,
        })
      }
    } catch (error) {
      // Error retrieving data
    }
  }

  update() {
    console.error(this.state)
  }
  selectPhoto() {
    ImagePicker.showImagePicker(options, (response) => {
      console.log('Response = ', response);
      if (response.didCancel) {
        console.log('User cancelled image picker');
      }
      else if (response.error) {
        console.error('ImagePicker Error: ', response.error);
      }
      else {
        let source = { uri: response.uri }
        this.setState({
          imageSource: source,
          data: response.data,
          gambar : true
        })
        // console.error(gambar.uri)
      }
    })
  }

  uploadPhoto() {
    if(this.state.gambar){
    this.setState({
      loading: true
    })
    RNFetchBlob.fetch('POST', 'http://10.0.3.2:5000/api', {
      PIN: "159-141-713",
      // 'Content-Type': 'multipart/form-data',
    }, [
        { name: 'file', filename: 'image.jpg', type: 'image/png', data: RNFetchBlob.wrap(this.state.imageSource.uri) },
      ]).then((resp) => {
        let dataku = JSON.parse(resp.data)
        this.setState({
          kematangan: dataku[0],
          berat: dataku[1].toFixed(2),
          loading: false
        })
      }).catch((err) => {
        console.error(err)
      })
    }
    else{
      alert("Silahkan Pilih Gambar Terlebih Dahulu")
    }
  }

  render() {
    return (
      <Container style={{ backgroundColor: 'white' }}>
        <Header style={styles.headerStyle} androidStatusBarColor='#004600'>
          <Body>
            <Title style={styles.titleStyle}>Prediksi Kematangan dan Berat Tomat</Title>
          </Body>
        </Header>
        <View style={{ flex: 1 }}>
          <Content>
            <TouchableOpacity onPress={this.selectPhoto.bind(this)}>
              {this.state.imageSource !== null ?
                <Image
                  style={{
                    height: 200,
                    width: 200,
                    alignSelf: "center",
                    marginTop: 20,
                    borderRadius: 20
                  }}
                  source={this.state.imageSource} />
                :
                <Icon name='logo-apple' style={{ fontSize: 120, alignSelf: 'center', paddingTop: 20, }} />}
            </TouchableOpacity>
            <Button
              onPress={() => this.uploadPhoto()}
              block={true}
              style={styles.buttonStyle}>
              <Text style={styles.buttonTextStyle}>Prediksi</Text>
            </Button>
            {this.state.loading ? <ActivityIndicator size="large" /> : <View><Text> </Text></View>}
            {this.state.kematangan ?
              <View>
                <View style={styles.row}>
                  <Text style={styles.kematangan1}>Tingkat Kematangan</Text>
                  <Text style={styles.berat1}>Perkiraan Berat</Text>
                </View>

                <View style={styles.row}>
                  <Text style={styles.kematangan2}>{this.state.kematangan}</Text>
                  <Text style={styles.berat2}>{this.state.berat} Gram</Text>
                </View>
              </View>
              : <View />
            }
          </Content>
        </View>
      </Container>
    );
  }
}