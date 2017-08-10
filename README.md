# README

The overall bookings data was scraped from https://sheriff.boco.solutions/JailOpenData/Home/JailBooking, so it has all of those columns. (`Name,Booking No,Booked,Location,DOB,Race,Sex,Case No,Arresting Agency,Charge,Arrest Date`)


The data from the records request had these columns: `'Booking Number', 'Name', 'Address', 'City', 'State', 'ZIP Code', 'Race', 'Sex', 'DOB', 'Booking Date', 'Booking Time', 'Facility', 'Location', 'Arresting Agency', 'Charge', 'Title', 'Charge Level'`. It's mostly similar, except it also includes "Address", "Facility", and "Charge Level". Since these are only records of homeless people, the "Address" field is almost always either empty, "Homeless", or "Transient" (when it's not some custom thing someone typed up, that luckily the Sheriff's office disambiguated for us).


Both of these datasets have each charge as a row, so a single booking will have multiple rows, one for each charge. To collapse it down so each row was a booking, I didn't want to discard the "charge" information, but it was hard to combine row-wise. So I did a compromise and added a column for each anti-homeless ordinance posted on this DU website (https://www.law.du.edu/index.php/homeless-advocacy-policy-project/anti-homeless-ordinance-tracker), then did string matches for those ordinances in the "Charge" column. If a charge matched, I marked the entire booking as `true` for that column, as well as for the `antihomeless` column. So `antihomeless` is true if any of the anti-homeless ordinances appeared as any of a booking's charges.

Those columns are `Name,Booked,Location,DOB,Race,Sex,Case No,Arresting Agency,Arrest Date,camping,fta,ftc,booking_time,boulder,urination,vehicle_as_residence,public_obstruct,public_trespass,begging,antihomeless,smoking,any_antihomeless,Address,City,State,ZIP Code,Booking Date,Booking Time,Facility,transient`


`fta` is "Failure to Appear"

`ftc` is "Failure to Comply"

Often columns will be both an anti-homeless ordinance and one of these two columns. For example, someone who got a court date for violating the camping ban and then didn't show up in court will have as their charge `FTA: CAMPING` or something. Homeless people often get charged multiple times for a single offense since they'll get hit with FTA when they don't show up to court.


The other lower case columns are ones that I added and should be sort of self-explanatory. Most are indicator variables for ordinances. `transient` is true if that booking showed up in the transient bookings dataset.
