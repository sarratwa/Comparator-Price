import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ShopService {

  readonly rootUrl : string = 'http://localhost:3000/products';
  constructor(private htppClient  :HttpClient) { }

  public get(){
    return this.htppClient.get(this.rootUrl)
  }

  public getOne(id : any){
    return this.htppClient.get(`http://localhost:3000/product-detail/${id}`)
  }

  public post(uri : string, payload : object){
    return this.htppClient.post(`${this.rootUrl}/${uri}`, payload)
  }

  public put(uri : string, payload : object){
    return this.htppClient.put(`${this.rootUrl}/${uri}`, payload)
  }
  
  public delete(uri : string){
    return this.htppClient.delete(`${this.rootUrl}/${uri}`)
  }

}
