from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<h1>HELLO WORLD</h1>")

def about_us(request):
    return HttpResponse("<h1>Welcome to About Us Page</h1>")


def contact(request):
    return HttpResponse("""
        <table border=10>
            <tr>
                <td>
                    <ul>
                        <li>Email: </li>
                        <ol>
                            <li>a@gmail.com</li>
                            <li>b@gmail.com</li>
                        </ol>
                        <li>Phone: +91 12345 67890</li>
                        <li>Address: BVVS Campus, Karnataka, India</li>
                    </ul>
                </td>
            </tr>
        </table>
    """)

