import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import Product from 'src/app/models/products';
import { ShopService } from 'src/app/services/shop.service';

@Component({
  selector: 'app-shop',
  templateUrl: './shop.component.html',
  styleUrls: ['./shop.component.css']
})
export class ShopComponent implements OnInit {

  filter : string ="All";
  products : Product[] = [];
  productsFilteredID = [];
  title : any;
  p:number = 1;
  constructor(
    private shopService : ShopService,
    private router: Router) { }

  ngOnInit() {
    if (this.filter == "All"){
      //after the task component is loaded this code is executed
      this.shopService.get()
        .subscribe((products : Product[]) =>
          this.products = products)
      //when we use the http client module from angular we get the result back
      //as an observale that allows us to use fct with asynchronus data
    }
  }

  goToDetail(id :number) {
    this.router.navigate([`product-detail/${id}`]);
  }

  Search(){
    if(this.title == ""){
      this.ngOnInit();
    }else {
      this.products = this.products.filter(res => {
        return res.title.toLocaleLowerCase().match(this.title.toLocaleLowerCase());
      })
    }
  }

  key: string="price"
  reverse: boolean = false
  sort(key) {
    this.key = key;
    this.reverse = !this.reverse
  }

}
