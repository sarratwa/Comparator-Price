import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ShopService } from 'src/app/services/shop.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  products : any;
  constructor(
    private router: Router,
    private shopService:ShopService) { }

  ngOnInit() {
    this.shopService.get()
      .subscribe(products => 
        this.products = products);
  }

}
