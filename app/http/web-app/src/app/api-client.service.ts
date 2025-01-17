import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiClientService {
  constructor(private http: HttpClient) {
  }

  createKudo(repo) {
    return this.perform('post', '/kudos', repo);
  }

  deleteKudo(repo) {
    return this.perform('delete', `/kudo/${repo.id}`);
  }

  updateKudo(repo) {
    return this.perform('put', `/kudos/${repo.id}`, repo);
  }

  getKudos() {
    return this.perform('get', '/kudos');
  }

  getKudo(repo) {
    return this.perform('get', `/kudo/${repo.id}`);
  }

  async perform(method, resource, data = {}) {
    const url = `http://localhost:4433${resource}`;

    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    };

    switch (method) {
      case 'delete':
        return this.http.delete(url, httpOptions).toPromise();
      case 'get':
        return this.http.get(url, httpOptions).toPromise();
      default:
        return this.http[method](url, data, httpOptions).toPromise();
    }
  }
}
