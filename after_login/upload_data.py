import streamlit as st
import pandas as pd

# Upload Data Page
st.title("📤 Upload Your Transaction Data")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state["transaction_data"] = df  # Store in session state
    st.success("File uploaded successfully!")
    st.write("### Preview of Uploaded Data:")
    st.dataframe(df.head())


# # upload_data.py
# import streamlit as st
# import pandas as pd
# from st_aggrid import AgGrid, GridUpdateMode, GridOptionsBuilder

# # Initialize shared DataFrame, file name, income_df, expense_df, and grid_options in session state
# if "shared_df" not in st.session_state:
#     st.session_state.shared_df = None
# if "uploaded_file_name" not in st.session_state:
#     st.session_state.uploaded_file_name = None
# if "grid_options" not in st.session_state:  # Store grid options here!
#     st.session_state.grid_options = None

# def update_shared_df(shared_df, updated_df, id_column):
#     """Updates shared_df based on changes in updated_df using id_column."""

#     # Ensure the id_column exists in both dataframes, if not create a new one for shared_df
#     if id_column not in shared_df.columns:
#         shared_df[id_column] = range(len(shared_df))  # create a new id column
#     if id_column not in updated_df.columns:
#         updated_df[id_column] = range(len(updated_df))  # create a new id column

#     merged_df = pd.merge(shared_df, updated_df, on=id_column, how='left', suffixes=('', '_updated'))

#     for col in updated_df.columns:
#         if col != id_column:
#             # Correctly use .values to get the NumPy array
#             mask = merged_df[col + '_updated'].notna().values  # Get boolean NumPy array
#             shared_df.loc[mask, col] = merged_df.loc[merged_df[col + '_updated'].notna(), col + '_updated'].values
#     return shared_df

# def display_and_edit_table(df):
#     if st.session_state.grid_options is None:  # Create options if they don't exist
#         st.session_state.grid_options = create_grid_options(df)

#     grid_response = AgGrid(
#         df,
#         gridOptions=st.session_state.grid_options,  # Use stored options
#         height=400,
#         width='100%',
#         update_mode=GridUpdateMode.MODEL_CHANGED,
#         allow_unsafe_jscode=True,
#         key="editable_grid"  # Key is still important
#     )

#     updated_df = grid_response['data']
#     selected_rows = grid_response['selected_rows']
#     return updated_df, selected_rows

# def add_row(df):
#     new_row = pd.DataFrame([{}])  # Create an empty row
#     return pd.concat([df, new_row], ignore_index=True)

# def delete_selected_rows(df, selected_rows):
#     if isinstance(selected_rows, pd.Series):  # Handle single row selection
#         indices_to_drop = [selected_rows["_index"]]  # Access _index directly
#     elif isinstance(selected_rows, list):  # Handle multiple row selection
#         indices_to_drop = [i["_index"] for i in selected_rows]
#     else:
#         return df  # No rows selected

#     updated_df = df.drop(indices_to_drop).reset_index(drop=True) # Reset index after dropping rows
#     return updated_df

# def save_changes(df, file_name):
#     try:
#         if file_name.endswith(".csv"):
#             df.to_csv(file_name, index=False)
#         else:
#             df.to_excel(file_name, index=False)
#         st.success("Changes saved successfully!")
#     except Exception as e:
#         st.error(f"Error saving file: {e}")

# def create_grid_options(df):  # Function to create/update grid options
#     gb = GridOptionsBuilder.from_dataframe(df)
#     gb.configure_selection(selection_mode="multiple", use_checkbox=True)
#     gb.configure_default_column(editable=True)
#     return gb.build()

# st.title("📤 Upload and Edit Your Transaction Data")

# # Main logic
# if st.session_state.shared_df is None:  # No DataFrame loaded
#     uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx", "xls"])

#     if uploaded_file:  # File uploaded
#         try:
#             if uploaded_file.name.endswith(".csv"):
#                 df = pd.read_csv(uploaded_file)
#                 df["ID"] = range(len(df)) # create a new column for ID
#             else:
#                 df = pd.read_excel(uploaded_file)
#                 df["ID"] = range(len(df)) 

#             st.session_state.shared_df = df.copy()
#             st.session_state.uploaded_file_name = uploaded_file.name
#             #update_income_expense_dfs(df)
#             st.rerun()  # Display table immediately

#         except Exception as e:
#             st.error(f"Error loading file: {e}")

# elif st.session_state.shared_df is not None:  # DataFrame loaded
#     df = st.session_state.shared_df
#     updated_df, selected_rows = display_and_edit_table(df) # Call display_and_edit_table

#     st.session_state.shared_df = updated_df  # Update the shared dataframe
#     #update_income_expense_dfs(updated_df)  # Update income/expense dfs

#     # ... (add/delete row and save logic - same as before)
#     col1, col2, col3 = st.columns(3)  # Use columns for better layout

#     with col1:
#         if st.button("Add Row"):
#             st.session_state.shared_df = add_row(st.session_state.shared_df)
#             st.session_state.grid_options = create_grid_options(st.session_state.shared_df)  # Update grid options
#             st.rerun()

#     with col2:
#         # Delete selected rows button
#         if st.button("Delete Selected Rows"):
#             #... (delete logic remains the same)
#             st.session_state.grid_options = create_grid_options(st.session_state.shared_df)  # Update grid options
#             st.rerun()

#             # Add download button
#         if st.session_state.shared_df is not None:
#             csv = st.session_state.shared_df.to_csv(index=False).encode('utf-8')
#             st.download_button(
#                 label="Download data as CSV",
#                 data=csv,
#                 file_name='downloaded_data.csv',
#                 mime='text/csv',
#             )
#             st.rerun()

#     with col3:
#         if st.button("Save Changes"):
#             save_changes(st.session_state.shared_df, st.session_state.uploaded_file_name)

#     if st.button("Clear Data"):  # Clear data and table
#         st.session_state.shared_df = None
#         st.session_state.uploaded_file_name = None  # Clear file name as well
#         st.session_state.grid_options = None  # Clear grid options too
#         st.rerun()



    




