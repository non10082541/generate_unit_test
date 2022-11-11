import {modules} from "./module.js";
import * as fs from 'fs';

const obj_module = new modules();

class unit_test{
  constructor()
  {
      this.file_name = './fb-game.json';
  }

  isObject = (obj) => {
      return typeof obj === 'object' && !Array.isArray(obj) && obj !== null;
    }
    
  objToArray = (obj) => {
      return Object.keys(obj).map((key) => {
        return [
          key, isObject(obj[key]) ? 
            objToArray(obj[key]) :
            obj[key]
        ];
      });    
    }

  async run() {

    let data = fs.readFileSync(this.file_name, 'utf-8');
    data = JSON.parse(data);

    let count_modules = Object.keys(data).length;
    console.log("count : " + count_modules);
    
    // console.log("data:", data[0].name)

    for (let i = 0; i < count_modules; i++){

      console.log("count:", i)
      console.log("***** begin module *****");

      try{

        await obj_module.execute(data[i]);

      }catch(err){

        console.log(err)

      }          
      console.log("***** end module *****");
      console.log("");
    }
  }
}

export {unit_test};