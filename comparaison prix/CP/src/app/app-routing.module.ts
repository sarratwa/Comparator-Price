import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { ProductDetailComponent } from './components/product-detail/product-detail.component';
import { ShopComponent } from './components/shop/shop.component';


const routes: Routes = [
  {path:'home', component:HomeComponent},
  {path:'shop', component:ShopComponent},
  {path:'home/shop', component:ShopComponent},
  {path:'product-detail/:id', component:ProductDetailComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
