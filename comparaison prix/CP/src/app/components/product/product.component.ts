import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import Product from 'src/app/models/products';
import { ShopService } from 'src/app/services/shop.service';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {

  product : any ;
  @Input() id : any;
  constructor(private shopService : ShopService,
    private router: Router) { }

  ngOnInit() {
    this.shopService.getOne(this.id)
      .subscribe((product : Product[]) =>
      this.product = product)
  }

  goToDetail(id :number) {
    this.router.navigate([`product-detail/${id}`]);
  }

}
