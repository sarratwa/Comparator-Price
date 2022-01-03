import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ShopService {

  shopUrl : string = 'http://localhost:3000';
  constructor(private htppClient  :HttpClient) { }

  getAllProducts(){
    return(this.htppClient.get<{products:any}>(this.shopUrl));
  }
}
