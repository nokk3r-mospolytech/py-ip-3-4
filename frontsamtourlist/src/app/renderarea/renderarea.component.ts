import {Component, Injectable, OnInit} from "@angular/core";
import {HttpService} from "../service/http.service";
import {FormControl} from '@angular/forms';
import {Location} from '@angular/common';


interface Interface {
  descriptions?: string
  id: number
  title: string
  Avilable_id: string
  ChillVariations_id: number
  Pricing_id: number
  Priority_id: number
  Region_id: number
}

@Component({
  selector: 'app-renderarea',
  templateUrl: './renderarea.component.html',
  styleUrls: ['./renderarea.component.scss']
})

@Injectable({providedIn: 'root'})


export class RenderareaComponent implements OnInit {

  constructor(private HttpService: HttpService, private location: Location) {
  }

  url =  "http://samsonovtourlist.std-936.ist.mospolytech.ru/api/v1/task/list"
  template = [] as unknown as Interface
  searchControl = new FormControl();
  request = [this.template]
  isActive = 'start'
  header = ''
  search = ''
  isDisable = false
  ranTitle = ''
  mainIsDisable = [true, 'Скрыть неактивные']

  ngOnInit(): void {

    this.recentPage(window.location.href)
    if (this.isActive != 'detail'){
      this.GetRequest(this.url)
    }
    this.searchTask()
  }

  searchTask(){
    this.searchControl.valueChanges
      .pipe()
      .subscribe(val => {
        this.search = val.toLowerCase().toString()
        console.log(this.search)
      });
  }

  recentPage(url:string){
    if (url.split('/').length == 3){
      this.isClicked(this.url, 'start', '')
      console.log('start')
    }
    if (url.split('/').length == 4 && url.split('/')[3] != ""){
      let res:string = url.split('/')[3]
      this.isClicked(this.url, 'main', res)
      console.log('next')
    }
    if (url.split('/').length == 5){
      let res:string = url.split('/')[3] + '/' + url.split('/')[4]
      this.isClicked(this.url + '/' + url.split('/')[4], 'detail', res)
      console.log('detail')
    }
  }

  changeRecentText(){
    let ran = Math.floor(Math.random() * (this.request.length))
    console.log(this.request)
    this.ranTitle = this.request[ran].title
  }

  mainChange(){
    if (this.mainIsDisable[0] == false) {
      this.mainIsDisable = [true, 'Скрыть неактивные']
    } else {
      this.mainIsDisable = [false, 'Показать неактивные']
    }
  }

  GetRequest(added_path?: string){
    if (added_path != undefined){
      this.HttpService.get(added_path).subscribe(value => {
        if (Array.isArray(value)){
          this.request = value
        } else {
          this.request = [value]
        }
        console.log(value)
        this.changeRecentText()
      }, err => {
        console.error(err)
      })
    }
  }

  isClicked(url: string, state: string, header?: string){
    switch (state){
      case "start": {
        this.isActive = "start"
        this.location.replaceState("")
        break
      }

      case "main": {
        this.isActive = "main"
        this.request = []
        this.GetRequest(url)
        if (header != null) {
          this.location.replaceState(header)
        }
        break
      }
      case "next": {
        this.isActive = "con"
        this.GetRequest(url)
        if (header != null) {
          this.location.replaceState(header)
        }
        break
      }
      case "detail": {
        this.isActive = "detail"
        this.request = []
        this.GetRequest(url)
        if (header != null) {
          this.location.replaceState(header)
        }
        break
      }
    }
  }

  //This is Development Functions. Deleted/Comment in prod versions!

  print(arr: any){
    console.log(arr)
  }
}

