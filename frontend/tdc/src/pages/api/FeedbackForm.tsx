import React from 'react';
{/* import { useFormik } from 'formik';
import * as Yup from 'yup'; */}

const FeedbackForm = () => {
    {/* const formik = useFormik({
    initialValues: {
        username: '',
        password: '',
    },
    validationSchema: Yup.object({
        username: Yup.string().required('Username is required'),
        password: Yup.string().required('Password is required'),
    }),
    onSubmit: (values) => {
        // Handle form submission and API requests here
    },
    }); */}
    const onSubmit = () => {
        console.log("test ran successfully!");
    };
    return (
      <div>
        {/* <form onSubmit={formik.handleSubmit}> */}
        <form onSubmit={() => onSubmit()}>
          <p>test</p>
        </form>
      </div>
    );
  };
  
export default FeedbackForm;
