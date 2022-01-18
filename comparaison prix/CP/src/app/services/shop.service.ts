import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ShopService {

  readonly rootUrl : string = 'http://localhost:3000';
  constructor(private htppClient  :HttpClient) { }

  public get(){
    //return this.htppClient.get(`${this.rootUrl}/${uri}`)
    return this.htppClient.get('products')
  }

  public post(uri : string, payload : object){
    return this.htppClient.get(`${this.rootUrl}/${uri}`, payload)
  }

  public put(uri : string, payload : object){
    return this.htppClient.get(`${this.rootUrl}/${uri}`, payload)
  }
  
  public delete(uri : string){
    return this.htppClient.get(`${this.rootUrl}/${uri}`)
  }

}
