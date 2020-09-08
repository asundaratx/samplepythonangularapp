import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  constructor(private router: Router) {
  }

  async ngOnInit() {
    const isAuthenticated = true;
    if (isAuthenticated) {
      this.router.navigate(['/home'], {replaceUrl: true})
    }
  }

  async login(event) {
    event.preventDefault();
    this.router.navigate(['/home'], {replaceUrl: true})
  }
}
