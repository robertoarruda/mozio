# Mozio

## Prerequisites
- Python 3.10 `sudo apt install python3.10`
- Pip `sudo apt install python-pip`
- VirtualEnv `sudo pip install virtualenv`

## Installation

### Clone the project:
```
git clone git@github.com:robertoarruda/mozio.git
```

### Enter the project directory:
```
cd ./mozio
```

### Create the Environment:
Within the project root, run the command below:
```
virtualenv venv --python=python3.10
```

### Activate the environment:
Run the command below to enable:
```
source venv/bin/activate
```

### Install dependencies:
Run the command below to install the project dependencies:
```
pip install -r requirements.txt
```

### Run API:
Execute the command below to run the crawler:
```
python manage.py manage.py runserver 0.0.0.0:8000
```

### Turn off the environment:
Execute the command below to deactivate:
```
deactivate
```

## Online demo

Documentation: [http://67.205.179.16:8000/provider/](http://67.205.179.16:8000/provider/)

### Provider

- [GET] /provider/
```
// Response
[
    {
        "_id": "9d2b85918f1f262230ff4919"
        "name": "Provider Name",
        "email": "test@test.com",
        "phone_number": "+5511991009887",
        "language": "language",
        "currency": "BRL"
    }
]
```

- [POST] /provider/
```
// Body
{
    "name": "Provider Name",
    "email": "test@test.com",
    "phone_number": "+5511991009887",
    "language": "language",
    "currency": "BRL"
}
```

- [GET] /provider/[id]
```
// Response
{
    "_id": "9d2b85918f1f262230ff4919"
    "name": "Provider Name",
    "email": "test@test.com",
    "phone_number": "+5511991009887",
    "language": "language",
    "currency": "BRL"
}
```

- [PUT] /provider/[id]
```
// Body
{
    "name": "Provider Name UPDATED",
    "email": "test@test.com",
    "phone_number": "+5511991009887",
    "language": "language",
    "currency": "BRL"
}
```

- [PATCH] /provider/[id]
```
// Body
{
    "name": "Provider Name UPDATED"
}
```

- [DELETE] /provider/[id]
```
// No content
```

### Service area

- [GET] /provider/service_area
```
// Response
[
    {
        "_id": "f530f9184f1d2b89f2262991",
        "provider_id": "9d2b85918f1f262230ff4919",
        "name": "Service area",
        "price": 100.0,
        "location": {
            "type": "Polygon",
            "coordinates": [[[-73.958, 40.8003], [-73.9498, 40.7968], [-73.9737, 40.7648], [-73.9814, 40.7681], [-73.958, 40.8003]]]
        }
    }
]
```

- [POST] /provider/service_area
```
// Body
{
	"provider_id": "9d2b85918f1f262230ff4919",
	"name": "Service area",
	"price": 100.0,
	"location": {
		"type": "Polygon",
		"coordinates": [[[-73.958, 40.8003], [-73.9498, 40.7968], [-73.9737, 40.7648], [-73.9814, 40.7681], [-73.958, 40.8003]]]
	}
}
```

- [GET] /provider/service_area/[id]
```
// Response
{
    "_id": "f530f9184f1d2b89f2262991",
	"provider_id": "9d2b85918f1f262230ff4919",
	"name": "Service area",
	"price": 100.0,
	"location": {
		"type": "Polygon",
		"coordinates": [[[-73.958, 40.8003], [-73.9498, 40.7968], [-73.9737, 40.7648], [-73.9814, 40.7681], [-73.958, 40.8003]]]
	}
}
```

- [PUT] /provider/service_area/[id]
```
// Body
{
    "_id": "f530f9184f1d2b89f2262991",
	"provider_id": "9d2b85918f1f262230ff4919",
	"name": "Service area UPDATED",
	"price": 100.0,
	"location": {
		"type": "Polygon",
		"coordinates": [[[-73.958, 40.8003], [-73.9498, 40.7968], [-73.9737, 40.7648], [-73.9814, 40.7681], [-73.958, 40.8003]]]
	}
}
```

- [PATCH] /provider/service_area/[id]
```
// Body
{
    "name": "Service area UPDATED"
}
```

- [DELETE] /provider/service_area/[id]
```
// No content
```

### List providers by service area location

- [GET] /provider/by_service_area_location/?lat=[lat]&lng=[lng]
```
// Response
[
	{
        "_id": "9d2b85918f1f262230ff4919"
        "name": "Provider Name",
        "email": "test@test.com",
        "phone_number": "+5511991009887",
        "language": "language",
        "currency": "BRL"
		'service_areas': [
			{
                "_id": "f530f9184f1d2b89f2262991",
                "provider_id": "9d2b85918f1f262230ff4919",
                "name": "Service area",
                "price": 100.0,
                "location": {
                    "type": "Polygon",
                    "coordinates": [[[-73.958, 40.8003], [-73.9498, 40.7968], [-73.9737, 40.7648], [-73.9814, 40.7681], [-73.958, 40.8003]]]
                }
			}
		]
	},
	{
        "_id": "2230ff49d2b85f26918f1919"
        "name": "Provider Name 2",
        "email": "test2@test.com",
        "phone_number": "+5514991098870",
        "language": "language",
        "currency": "BRL"
		'service_areas': [
			{
                "_id": "d2b89f22f530f9184f162991",
                "provider_id": "2230ff49d2b85f26918f1919",
                "name": "Service area 2",
                "price": 50.0,
                "location": {
                    "type": "Polygon",
                    "coordinates": [[[-73.958, 40.8003], [-73.9498, 40.7968], [-73.9737, 40.7648], [-73.9814, 40.7681], [-73.958, 40.8003]]]
                }
			}
		]
	}
]
```