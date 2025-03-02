export const getImgSrc = ( name:string ) => {
   
    const path = `/images/${name}`
    return path
    
    // const modules = import.meta.glob('/src/assets/photos/*.png', { eager: true }) 
  
    // return (modules[path] as any).default
}
