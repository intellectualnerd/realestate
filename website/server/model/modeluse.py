import sys
import joblib
import numpy as np

model_path = 'D:/Projects/Real Estate Prediction/website/server/model/model_joblib'

# Load the model
mymodel = joblib.load(model_path)
X =np.array(['x','y','z','Devarachikkanahalli', '1st Block Jayanagar',
       '1st Block Koramangala', '1st Phase JP Nagar',
       '2nd Phase JP Nagar', '2nd Phase Judicial Layout',
       '2nd Stage Nagarbhavi', '4th Block Koramangala',
       '5th Block Hbr Layout', '5th Phase JP Nagar', '6th Phase JP Nagar',
       '7th Phase JP Nagar', '8th Phase JP Nagar', '9th Phase JP Nagar',
       'AECS Layout', 'Abbigere', 'Akshaya Nagar', 'Ambalipura',
       'Ambedkar Nagar', 'Amruthahalli', 'Anandapura', 'Ananth Nagar',
       'Anekal', 'Anjanapura', 'Ardendale', 'Arekere', 'Attibele',
       'B Narayanapura', 'BEML Layout', 'BTM 1st Stage', 'BTM 2nd Stage',
       'BTM Layout', 'Babusapalaya', 'Badavala Nagar', 'Balagere',
       'Banagiri Nagar', 'Banashankari', 'Banashankari Stage II',
       'Banashankari Stage III', 'Banashankari Stage V',
       'Banashankari Stage VI', 'Banaswadi', 'Banjara Layout',
       'Bannerghatta', 'Bannerghatta Road', 'Basapura', 'Basavangudi',
       'Basaveshwara Nagar', 'Battarahalli', 'Begur', 'Begur Road',
       'Bellandur', 'Benson Town', 'Bharathi Nagar', 'Bhoganhalli',
       'Billekahalli', 'Binny Pete', 'Bisuvanahalli', 'Bommanahalli',
       'Bommasandra', 'Bommasandra Industrial Area', 'Bommenahalli',
       'Brookefield', 'Budigere', 'CV Raman Nagar', 'Chamrajpet',
       'Chandapura', 'Chandra Layout', 'Channasandra', 'Chennammana Kere',
       'Chikka Tirupathi', 'Chikkabanavar', 'Chikkalasandra',
       'Choodasandra', 'Cooke Town', 'Cox Town', 'Cunningham Road',
       'Dairy Circle', 'Dasanapura', 'Dasarahalli', 'Devanahalli',
       'Dodda Nekkundi', 'Doddaballapur', 'Doddakallasandra',
       'Doddathoguru', 'Dodsworth Layout', 'Domlur', 'Dommasandra',
       'EPIP Zone', 'Ejipura', 'Electronic City',
       'Electronic City Phase II', 'Electronics City Phase 1',
       'Frazer Town', 'GM Palaya', 'Ganga Nagar', 'Garudachar Palya',
       'Giri Nagar', 'Gollahalli', 'Gollarapalya Hosahalli', 'Gottigere',
       'Green Glen Layout', 'Gubbalala', 'Gunjur', 'Gunjur Palya',
       'HAL 2nd Stage', 'HBR Layout', 'HRBR Layout', 'HSR Layout',
       'Haralur Road', 'Harlur', 'Hebbal', 'Hebbal Kempapura',
       'Hegde Nagar', 'Hennur', 'Hennur Road', 'Hoodi', 'Horamavu Agara',
       'Horamavu Banaswadi', 'Hormavu', 'Hosa Road', 'Hosakerehalli',
       'Hoskote', 'Hosur Road', 'Hulimavu', 'ISRO Layout', 'ITPL',
       'Iblur Village', 'Indira Nagar', 'JP Nagar', 'Jakkur',
       'Jakkur Plantation', 'Jalahalli', 'Jalahalli East', 'Jigani',
       'Judicial Layout', 'KR Puram', 'KUDLU MAIN ROAD',
       'Kadubeesanahalli', 'Kadugodi', 'Kaggadasapura', 'Kaggalipura',
       'Kaikondrahalli', 'Kalena Agrahara', 'Kalkere', 'Kalyan nagar',
       'Kamakshipalya', 'Kambipura', 'Kammanahalli', 'Kammasandra',
       'Kanakapura', 'Kanakpura Road', 'Kannamangala', 'Karuna Nagar',
       'Kasavanhalli', 'Kasturi Nagar', 'Kathriguppe', 'Kaval Byrasandra',
       'Kaverappa Layout', 'Kenchenahalli', 'Kengeri',
       'Kengeri Satellite Town', 'Kereguddadahalli', 'Kodichikkanahalli',
       'Kodigehaali', 'Kodigehalli', 'Kodihalli', 'Kogilu', 'Konanakunte',
       'Koramangala', 'Kothannur', 'Kothanur', 'Kudlu', 'Kudlu Gate',
       'Kumaraswami Layout', 'Kundalahalli', 'LB Shastri Nagar',
       'Laggere', 'Lakshminarayana Pura', 'Lingadheeranahalli',
       'Lingarajapuram', 'Magadi Road', 'Mahadevpura',
       'Mahalakshmi Layout', 'Mallasandra', 'Malleshpalya',
       'Malleshwaram', 'Marathahalli', 'Margondanahalli', 'Marsur',
       'Mathikere', 'Medahalli', 'Mico Layout', 'Munnekollal',
       'Murugeshpalya', 'Mysore Road', 'NGR Layout', 'NRI Layout',
       'Nagadevanahalli', 'Naganathapura', 'Nagappa Reddy Layout',
       'Nagarbhavi', 'Nagasandra', 'Nagavara', 'Nagavarapalya',
       'Narayanapura', 'Neeladri Nagar', 'Nehru Nagar', 'OMBR Layout',
       'Old Airport Road', 'Old Madras Road', 'Padmanabhanagar',
       'Pai Layout', 'Panathur', 'Parappana Agrahara',
       'Pattandur Agrahara', 'Peenya', 'Poorna Pragna Layout',
       'Prithvi Layout', 'R.T. Nagar', 'Rachenahalli',
       'Raja Rajeshwari Nagar', 'Rajaji Nagar', 'Rajiv Nagar',
       'Ramagondanahalli', 'Ramamurthy Nagar', 'Rayasandra',
       'Richmond Town', 'Sadashiva Nagar', 'Sahakara Nagar',
       'Sanjay nagar', 'Sarakki Nagar', 'Sarjapur', 'Sarjapur  Road',
       'Sarjapura - Attibele Road', 'Sector 1 HSR Layout',
       'Sector 2 HSR Layout', 'Sector 7 HSR Layout', 'Seegehalli',
       'Shampura', 'Shivaji Nagar', 'Singasandra', 'Somasundara Palya',
       'Sompura', 'Sonnenahalli', 'Subramanyapura', 'Sultan Palaya',
       'TC Palaya', 'Talaghattapura', 'Thanisandra', 'Thigalarapalya',
       'Thubarahalli', 'Thyagaraja Nagar', 'Tindlu', 'Tumkur Road',
       'Ulsoor', 'Uttarahalli', 'Varthur', 'Varthur Road', 'Vasanthapura',
       'Vidyaranyapura', 'Vignana Nagar', 'Vijayanagar',
       'Vishveshwarya Layout', 'Vishwanatha Nagenahalli',
       'Vishwapriya Layout', 'Vittasandra', 'Whitefield',
       'Yelachenahalli', 'Yelahanka', 'Yelahanka New Town', 'Yelenahalli',
       'Yemlur', 'Yeshwanthpur', 'other'])

def predict_price(location,sqft,bath,bhk):    
    x = np.zeros(278)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    #search loc index
    #np.where list ==> 1st ele ==> 1st ele
    loc_index = np.where(X==location)[0]
    #makes 1 where locaion is
    if loc_index >= 0:
        x[loc_index] = 1

    print(mymodel.predict([x])[0])    

location_data = sys.argv[1]
bhk_data = sys.argv[2]
bath_data = sys.argv[3]
sqft_data = sys.argv[4]

predict_price(location_data,sqft_data,bath_data,bhk_data)