/* 
  아래에 코드를 작성해주세요.
  */
  const searchBtn = document.querySelector('.search-box__button')
  const keyword1 = document.querySelector('.search-box__input')

function fetchAblums(event) {
  const keyword = document.querySelector('.search-box__input')
  const myAPI = 'd0dd90604a9c595a18c209ddf32bef64'
  const API_URI = `https://ws.audioscrobbler.com/2.0/?method=album.search&album=${keyword.value}&api_key=${myAPI}&format=json`
  let page = 1
  let limit = 10
  axios(
    {
      method:'get',
      url:API_URI
    }
  )
  .then ((response) => {
    const albums = response.data.results.albummatches.album
    albums.forEach(element => {
      const divTag = document.createElement('div')
      divTag.classList.add("search-result__card")
      const imgTag = document.createElement('img')
      imgsrc = element.image[1]['#text']
      imgTag.setAttribute('src', imgsrc)
      divTag.appendChild(imgTag)
      const divTag2 = document.createElement('div')
      divTag2.classList.add("search-result__text")
      divTag.appendChild(divTag2)
      const h2Tag = document.createElement('h2')
      h2Tag.innerText=element.artist
      divTag2.appendChild(h2Tag)
      const pTag = document.createElement('p')
      pTag.innerText=element.name
      divTag2.appendChild(pTag)
      const divtag3 = document.querySelector('.search-result')
      divtag3.appendChild(divTag)
      function loop(event) {
        location.href = element.url
      }
      divTag.addEventListener('click', loop)
    });
  }) 
  .catch ((error) => {
    alart('잠시 후 다시 시도해주세요')
  })
  keyword.value=null
}
searchBtn.addEventListener('click', fetchAblums)
keyword1.addEventListener('keypress', function (event) {
  if (event.keyCode === 13) {
    fetchAblums()
  } 
})
