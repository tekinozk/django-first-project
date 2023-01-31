

CONTACT_DETAIL = '''
 <div class="container">
        <div class="row mb-5">
            <div class="col-sm-8 offset-sm-2">
                <h2>Adresimiz</h2>
                <address>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt non architecto quidem error velit
                        tempora quisquam aut, quo perspiciatis cupiditate!</p>
                </address>
                <hr>
                <h2 class="mt-5">Bize Ulasin</h2>
                <form class="row g-3">
                    <div class="col-12">
                        <label for="inputEmail4" class="form-label">Email</label>
                        <input type="email" class="form-control" id="inputEmail4">
                    </div>

                    <div class="col-12">
                        <label for="bilgi" class="form-label">Bilgi</label>
                        <textarea class="form-control" id="bilgi"></textarea>
                    </div>

                    <div class="col-12">
                        <label for="inputCity" class="form-label">Sehir</label>
                        <input type="text" class="form-control" id="inputCity">
                    </div>
                    <div class="col-12">
                        <label for="inputState" class="form-label">Bize Nasil Ulastin</label>
                        <select id="inputState" class="form-select">
                            <option selected>Seciminiz...</option>
                            <option>Sosyal Medya</option>
                            <option>Google</option>
                            <option>Reklam</option>
                            <option>Referams</option>
                        </select>
                    </div>


                    <div class="col-12">
                        <button type="submit" class="btn btn-primary">Gonder</button>
                    </div>
                </form>
            </div>
        </div>

        <!-- Projects -->
      
        <!-- Projects END -->


    </div>'''



FAKE_DB_PAGES = [

    {"url":"/contact/","detail":CONTACT_DETAIL }
]