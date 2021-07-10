import {Component, Injectable, OnInit} from "@angular/core";
import {HttpService} from "../service/http.service";
import {FormControl} from '@angular/forms';
import {Location} from '@angular/common';


interface Request {
  descriptions?: string
  id: number
  title: string
  Avilable_id: string
  ChillVariations_id: number
  Pricing_id: number
  Priority_id: number
  Region_id: number
}

interface Guide {
  id: number
  name: string
  Region_id?: string
  TaskDate_id?: string
  rating?: number
}

interface Bar {
  size: number
  name: string
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
  guideUrl = "http://samsonovtourlist.std-936.ist.mospolytech.ru/api/v1/guide/list"
  taskUrl =  "http://samsonovtourlist.std-936.ist.mospolytech.ru/api/v1/task/list"
  searchControl = new FormControl();
  request = [[] as unknown as Request]
  guideRequest = [[] as unknown as Guide]
  isActive = 'start'
  header = ''
  search = ''
  isDisable = false
  ranTitle = ''
  bars = [{size: 10, name: 'FF'},
    {size: 15, name: 'FF'},
    {size: 20, name: 'FF'},
    {size: 16, name: 'FF'},
    {size: 46, name: 'FF'},
    {size: 6, name: 'FF'},
    {size: 13, name: 'FF'},
    {size: 84, name: 'FF'} as unknown as Bar]
  mainIsDisable = [true, 'Скрыть неактивные']

  ngOnInit(): void {

    this.recentPage(window.location.href)
    if (this.isActive != 'detail'){
      this.GetRequest('request', this.taskUrl)
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
      this.isClicked(this.taskUrl, 'start', '')
      console.log('start')
    }
    if (url.split('/').length == 4 && url.split('/')[3] != ""){
      let res:string = url.split('/')[3]
      if (res == 'dashboard'){
        this.isClicked(this.taskUrl, 'dashboard', res)
      } else{
        this.isClicked(this.taskUrl, 'main', res)
      }
      console.log('next')
    }
    if (url.split('/').length == 5){
      let res:string = url.split('/')[3] + '/' + url.split('/')[4]
      this.isClicked(this.taskUrl + '/' + url.split('/')[4], 'detail', res)
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

  GetRequest(type: string, added_path?: string){
    if (added_path != undefined){
      this.HttpService.get(added_path).subscribe(value => {
        // console.log(value)
        switch (type) {
          case 'request':{
            if (Array.isArray(value)){
              this.request = value
            } else {
              this.request = [value]
            }
            this.changeRecentText()
            break
          }
          case 'guide':{
            if (Array.isArray(value)){
              this.guideRequest = value
            } else {
              this.guideRequest = [value]
            }
            break
          }
        }
      }, err => {
        console.error(err)
      })
    }
  }

  infoForDashboard(info:number):any{
    // console.log(this.request.length)
    let i = 0

    switch (info) {
      case 1:{
        for (let j in this.request){
          if (this.request[j].Avilable_id == 'Да'){
            i += 1
          }
        }
        return i
      }
      case 2:{
        for (let j in this.request){
          if (this.request[j].Avilable_id == 'Да'){
            i += 1
          }
        }
        return i
      }
      case 3:{
        for (let j in this.request){
          i += Number(this.request[j].Pricing_id)
        }
        return i
      }
    }

    return
  }

  infoForGist(info:number):any{
    // console.log(this.request.length)
    let i = 0

    switch (info) {
      case 1:{
        // i = Max size
        i = 100000
        for (let j in this.bars){
          if (this.bars[j].size <= i)
          i = this.bars[j].size
        }
        return i
      }
      case 2:{
        for (let j in this.bars){
          if (this.bars[j].size >= i)
            i = this.bars[j].size
        }
        return i
      }
      case 3:{
        for (let j in this.bars){
          i += Number(this.bars[j].size)
        }
        return i
      }
    }

    return
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
        this.GetRequest('request', url)
        if (header != null) {
          this.location.replaceState(header)
        }
        break
      }
      case "dashboard": {
        this.isActive = "dashboard"
        this.request = []
        this.GetRequest('request', url)
        this.GetRequest('guide', this.guideUrl)
        if (header != null) {
          this.location.replaceState(header)
        }
        break
      }
      case "next": {
        this.isActive = "con"
        this.GetRequest('request', url)
        if (header != null) {
          this.location.replaceState(header)
        }
        break
      }
      case "detail": {
        this.isActive = "detail"
        this.request = []
        this.GetRequest('request', url)
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

